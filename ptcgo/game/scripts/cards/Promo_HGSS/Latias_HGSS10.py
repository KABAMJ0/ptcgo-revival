from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import named_in_play
from ptcgo.game.card_effects.support_common import search_attach_energy

async def infinite_wind(ctx):
    """40; and with Latios on the Bench, 2 counters off each of your Benched."""
    await ctx.deal_damage(40)
    if not named_in_play("Latios", side="mine")(ctx):
        return
    for pokemon in ctx.my_bench():
        await ctx.heal(20, pokemon)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e196bb68-5191-556f-8128-9152934b85f8",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Latias.Name",
    display_name="Latias",
    searchable_by=["Latias", "Basic", "Latias"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.COLORLESS,
    family_id=380,
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Search your discard pile for a basic Energy card and attach it to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=search_attach_energy(count=1, distribute=True),
        ),
        Attack(
            title="Infinite Wind",
            game_text="If Latios is on your Bench, remove 2 damage counters from each of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=infinite_wind,
        ),
    ],
)