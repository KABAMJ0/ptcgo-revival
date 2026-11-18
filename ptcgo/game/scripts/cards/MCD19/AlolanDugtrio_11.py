from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="19ae0dc1-dda4-55d1-a751-ebb2221ce6b8",
    key="MCD19",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDugtrio.Name",
    display_name="Alolan Dugtrio",
    searchable_by=["Alolan Dugtrio", "Stage 1", "AlolanDugtrio"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="MCD19",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name",
    family_id=51,
    abilities=[
        Attack(
            title="Gold Rush",
            game_text="Discard any number of Metal Energy cards from your hand. This attack does 30 damage for each card you discarded in this way.",
            cost={},
            damage=30,
            effect=unimplemented,
        ),
    ],
)