from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import bare_mill
from ptcgo.game.content.definitions import def_for
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.card_effects.attacks_common import spread_damage

class FrenzyPassive(Passive):
    """Attacks do 40 more to the Defending Pokemon while the opponent has any of
    the named Pokemon in play."""

    NAMES = ('Kyogre', 'Kyogre ex', 'Rayquaza', 'Rayquaza ex')

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.attacker is None or carrier_pokemon(carrier) is not calc.attacker:
            return
        if not getattr(calc, "to_active", False):
            return
        for player_id in calc.board.player_ids:
            if player_id == calc.attacker.owning_player_id:
                continue
            for pokemon in calc.board.pokemon_in_play(player_id):
                definition = def_for(pokemon.archetype_id)
                if definition is not None and definition.display_name in self.NAMES:
                    calc.amount += 40
                    return



async def mix_up(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Mix-Up")
    if results and results[0]:
        await bare_mill(1, opponent=True)(ctx)

card = PokemonCardDef(
    guid="76fa6e08-c99a-5e14-9c35-55da152375dd",
    key="NP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudonex.Name",
    display_name="Groudon ex",
    searchable_by=["Groudon ex", "Basic", "EX", "Groudonex"],
    subtypes=["Basic", "EX"],
    collector_number=38,
    set_code="NP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=383,
    abilities=[
        Ability(
            title="Frenzy",
            game_text="As long as your opponent has Kyogre, Kyogre ex, Rayquaza, or Rayquaza ex in play, Groudon ex's attacks do 40 more damage to the Defending Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=FrenzyPassive(),
        ),
        Attack(
            title="Mix-Up",
            game_text="Flip a coin. If heads, your opponent discards the top card from his or her deck.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=mix_up,
        ),
        Attack(
            title="Earthquake",
            game_text="Does 10 damage to each of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=spread_damage(10, side="mine"),
        ),
    ],
)