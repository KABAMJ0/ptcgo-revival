from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="68edbde5-8fd4-5645-a170-3689993aff8c",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kilowattrel.Name",
    display_name="Kilowattrel",
    searchable_by=["Kilowattrel", "Stage 1", "Kilowattrel"],
    subtypes=["Stage 1"],
    collector_number=79,
    set_code="SV1",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wattrel.Name",
    family_id=940,
    abilities=[
        Attack(
            title="Skill Dive",
            game_text="This attack does 50 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Thunder Blast",
            game_text="Discard a Lightning Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=140,
            effect=unimplemented,
        ),
    ],
)