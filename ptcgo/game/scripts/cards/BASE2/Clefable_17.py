from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def metronome(ctx):
    """Choose 1 of the Defending Pokemon's attacks and use it as this attack,
    ignoring that attack's Energy costs and any other requirement."""
    defender = ctx.defender
    if defender is None:
        return
    candidates = [(defender, attack) for attack in ctx.attacks_of(defender)]
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(candidates, "Choose an attack to copy")
    if picked is None:
        return
    source, chosen = picked
    await ctx.use_attack(chosen, source=source)

card = PokemonCardDef(
    guid="794c75a5-d857-55e8-9d01-bbdfbc53dcdc",
    key="BASE2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefable.Name",
    display_name="Clefable",
    searchable_by=["Clefable", "Stage 1", "Clefable"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="BASE2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    family_id=36,
    abilities=[
        Attack(
            title="Metronome",
            game_text="Choose 1 of the Defending Pok\u00e9mon's attacks. Metronome copies that attack except for its Energy costs and anything else required in order to use that attack, such as discarding Energy cards. (No matter what type the Defending Pok\u00e9mon is, Clefable's type is still Colorless.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=metronome,
        ),
        Attack(
            title="Minimize",
            game_text="All damage done by attacks to Clefable during your opponent's next turn is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)