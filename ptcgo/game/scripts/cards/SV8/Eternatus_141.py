from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.trainers import is_pokemon_ex
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def high_pressure_blast(ctx):
    """Discard a Stadium in play. If you can't, this attack does nothing."""
    discarded = await ctx.discard_stadium()
    if discarded is None:
        return
    await ctx.deal_damage()

card = PokemonCardDef(
    guid="8188a463-b115-5a17-90bb-2163c22d9210",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eternatus.Name",
    display_name="Eternatus",
    searchable_by=["Eternatus", "Basic", "Eternatus"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=890,
    abilities=[
        Attack(
            title="Dyna-Blast",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex, this attack does 80 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_pokemon_ex(ctx.defender), 80),
        ),
        Attack(
            title="World Ender",
            game_text="Discard a Stadium in play. If you can't, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.DARKNESS: 2},
            damage=230,
            effect=high_pressure_blast,
        ),
    ],
)