from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f15a1d84-8f64-5f98-88d3-2b0b1c1043a2",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farigiraf.Name",
    display_name="Farigiraf",
    searchable_by=["Farigiraf", "Stage 1", "Farigiraf"],
    subtypes=["Stage 1"],
    collector_number=155,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    family_id=203,
    abilities=[
        Attack(
            title="Either Face",
            game_text="Choose a player. That player shuffles their hand into their deck and draws 4 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Power Beam",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
        ),
    ],
)