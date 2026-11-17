from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4dde62bb-a606-5bbb-8ef5-0c7321889feb",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    display_name="Abra",
    searchable_by=["Abra", "Basic", "Abra"],
    subtypes=["Basic"],
    collector_number=80,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=63,
    abilities=[
        Ability(
            title="Teleporter",
            game_text="Once during your turn, if this Pok\u00e9mon is in the Active Spot, you may shuffle it and all attached cards into your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)