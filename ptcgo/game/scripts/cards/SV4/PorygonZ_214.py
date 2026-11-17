from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="65644881-e514-5d94-8b1c-86241685886c",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.PorygonZ.Name",
    display_name="Porygon-Z",
    searchable_by=["Porygon-Z", "Stage 2", "PorygonZ"],
    subtypes=["Stage 2"],
    collector_number=214,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Porygon2.Name",
    family_id=137,
    abilities=[
        Ability(
            title="Buggy Turbo",
            game_text="Once during your turn, you may flip a coin. If heads, attach up to 4 Basic Energy cards from your discard pile to this Pok\u00e9mon. If tails, discard an Energy from this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Energized Attack",
            game_text="This attack does 40 damage for each Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)