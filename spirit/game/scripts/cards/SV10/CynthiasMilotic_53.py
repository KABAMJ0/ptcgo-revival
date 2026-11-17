from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0eb49401-e4a6-5aba-9aee-239095f3be6c",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasMilotic.Name",
    display_name="Cynthia's Milotic",
    searchable_by=["Cynthia's Milotic", "Stage 1", "CynthiasMilotic"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.CynthiasFeebas.Name",
    family_id=349,
    abilities=[
        Attack(
            title="Aqua Split",
            game_text="This attack also does 30 damage to 2 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)