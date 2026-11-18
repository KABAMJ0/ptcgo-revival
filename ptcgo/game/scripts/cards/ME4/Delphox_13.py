from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="26e6326e-08b6-5e74-9da2-37ad0db0864a",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    display_name="Delphox",
    searchable_by=["Delphox", "Stage 2", "Delphox"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Braixen.Name",
    family_id=653,
    abilities=[
        Ability(
            title="Flaring Magic",
            game_text="Once during your turn, you may discard a Basic Fire Energy card from your hand in order to use this Ability. Draw cards until you have 7 cards in your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Energized Storm",
            game_text="This attack does 30 damage for each Energy attached to all Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)