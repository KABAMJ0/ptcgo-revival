from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fc35f2f8-2883-581d-9151-d1b2ed587b24",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Steelix.Name",
    display_name="Steelix",
    searchable_by=["Steelix", "Stage 1", "Prime", "Steelix"],
    subtypes=["Stage 1", "Prime"],
    collector_number=87,
    set_code="HGSS2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    family_id=95,
    abilities=[
        Ability(
            title="Perfect Metal",
            game_text="Steelix can't be affected by any Special Conditions",
            effect=unimplemented,
        ),
        Attack(
            title="Energy Stream",
            game_text="Search your discard pile for an Energy card and attach it to Steelix.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Gaia Crush",
            game_text="You may discard any Stadium card in play.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=unimplemented,
        ),
    ],
)