from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9a6592ff-4602-5d6b-bcdd-ad69c432df1d",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Prime", "Kingdra"],
    subtypes=["Stage 2", "Prime"],
    collector_number=85,
    set_code="HGSS2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Ability(
            title="Spray Splash",
            game_text="Once during your turn (before your attack), you may put 1 damage counter on 1 of your opponent's Pok\u00e9mon. This power can't be used if Kingdra is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Dragon Steam",
            game_text="If your opponent has any Fire Pok\u00e9mon in play, this attack's base damage is 20 instead of 60.",
            cost={PokemonTypes.WATER: 1},
            damage=60,
            effect=unimplemented,
        ),
    ],
)