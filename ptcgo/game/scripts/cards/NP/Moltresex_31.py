from ptcgo.game.card_effects.pokemon import is_fire_energy
from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.content.definitions import def_for
from ptcgo.game.session.passives import Passive, carrier_pokemon

class SynchronizedLiftPassive(Passive):
    """Retreat Cost is 0 while both partner birds are on the same side."""

    PARTNERS = ('Articuno ex', 'Zapdos ex')

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        names = set()
        for ally in board.pokemon_in_play(pokemon.owning_player_id):
            definition = def_for(ally.archetype_id)
            if definition is not None and definition.display_name:
                names.add(definition.display_name)
        return 0 if all(partner in names for partner in self.PARTNERS) else cost



async def flame_gift(ctx):
    await ctx.deal_damage()
    me = ctx.attacker
    others = [pokemon for pokemon in ctx.my_pokemon_in_play() if pokemon is not me]
    if not others:
        return
    await ctx.move_energy_freely(
        [me], others, predicate=is_fire_energy, max_count=1,
        prompt="Move a Fire Energy to another Pokémon",
    )

card = PokemonCardDef(
    guid="2e366da7-6668-5fdf-b439-dd7ea35bb7d7",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltresex.Name",
    display_name="Moltres ex",
    searchable_by=["Moltres ex", "Basic", "EX", "Moltresex"],
    subtypes=["Basic", "EX"],
    collector_number=31,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Ability(
            title="Synchronized Lift",
            game_text="As long as you have Articuno ex and Zapdos ex in play, the Retreat Cost for Moltres ex is 0.",
            passive=SynchronizedLiftPassive(),
        ),
        Attack(
            title="Flame Gift",
            game_text="You may move a Fire Energy card attached to Moltres ex to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flame_gift,
        ),
        Attack(
            title="Scorching Wing",
            game_text="Discard all Fire Energy attached to Moltres ex.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.FIRE),
        ),
    ],
)