from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="aa1e30dd-32bd-5ba5-a6e2-cc605e021324",
    key="RSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Galvantula.Name",
    display_name="Galvantula",
    searchable_by=["Galvantula", "Stage 1", "Galvantula"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="RSV10PT5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name",
    family_id=595,
    abilities=[
        Attack(
            title="Discharge",
            game_text="Discard all Lightning Energy from this Pok\u00e9mon. This attack does 50 damage for each card you discarded in this way.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=50,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)