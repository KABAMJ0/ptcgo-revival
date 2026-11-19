from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def _super_psywave(ctx):
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pok\u00e9mon")
    if target is None:
        return
    counters = len(ctx.attached_energies(target))
    if counters:
        await ctx.deal_damage(counters * 10, target=target, as_counters=True)

card = PokemonCardDef(
    guid="6769b785-3b44-570b-a040-9897955c806d",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Attack(
            title="Super Psywave",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. Count the number of Energy cards attached to that Pok\u00e9mon. Put that many damage counters on the Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=_super_psywave,
        ),
    ],
)