from ptcgo.game.card_effects.pokemon import is_water_energy
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.content.definitions import def_for
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.card_effects.attacks_common import condition_attack

class SynchronizedLiftPassive(Passive):
    """Retreat Cost is 0 while both partner birds are on the same side."""

    PARTNERS = ('Moltres ex', 'Zapdos ex')

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        names = set()
        for ally in board.pokemon_in_play(pokemon.owning_player_id):
            definition = def_for(ally.archetype_id)
            if definition is not None and definition.display_name:
                names.add(definition.display_name)
        return 0 if all(partner in names for partner in self.PARTNERS) else cost



async def ice_gift(ctx):
    await ctx.deal_damage()
    me = ctx.attacker
    others = [pokemon for pokemon in ctx.my_pokemon_in_play() if pokemon is not me]
    if not others:
        return
    await ctx.move_energy_freely(
        [me], others, predicate=is_water_energy, max_count=1,
        prompt="Move a Water Energy to another Pokémon",
    )

card = PokemonCardDef(
    guid="5e7ea981-0f05-5d00-b3d0-40caad4f77ae",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Articunoex.Name",
    display_name="Articuno ex",
    searchable_by=["Articuno ex", "Basic", "EX", "Articunoex"],
    subtypes=["Basic", "EX"],
    collector_number=32,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=144,
    abilities=[
        Ability(
            title="Synchronized Lift",
            game_text="As long as you have Zapdos ex and Moltres ex in play, the Retreat Cost for Articuno ex is 0.",
            passive=SynchronizedLiftPassive(),
        ),
        Attack(
            title="Ice Gift",
            game_text="You may move a Water Energy attached to Articuno ex to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=ice_gift,
        ),
        Attack(
            title="Freezing Wing",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Asleep.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.ASLEEP, flip=True),
        ),
    ],
)