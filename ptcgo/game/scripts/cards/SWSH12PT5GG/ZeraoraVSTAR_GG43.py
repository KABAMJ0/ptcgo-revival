from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

async def crushing_beat(ctx):
    """190. You may discard a Stadium in play."""
    await ctx.deal_damage()
    if ctx.stadium_in_play() and await ctx.ask_yes_no("Discard the Stadium in play?"):
        await ctx.discard_stadium()

card = PokemonCardDef(
    guid="f1973b68-9d1f-5022-a827-605f24cbc06e",
    key="SWSH12PT5GG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraVSTAR.Name",
    display_name="Zeraora VSTAR",
    searchable_by=["Zeraora VSTAR", "VSTAR", "ZeraoraVSTAR"],
    subtypes=["VSTAR"],
    collector_number=43,
    set_code="SWSH12PT5GG",
    rarity=Rarities.RareHoloVSTAR,
    hp=270,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.VSTAR,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.ZeraoraV.Name",
    family_id=807,
    abilities=[
        Attack(
            title="Crushing Beat",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=crushing_beat,
        ),
        Attack(
            title="Lightning Storm Star",
            game_text="Choose 1 of your opponent's Pok\u00e9mon 4 times. (You can choose the same Pok\u00e9mon more than once.) For each time you chose a Pok\u00e9mon, do 60 damage to it. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 VSTAR Power in a game.)",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)