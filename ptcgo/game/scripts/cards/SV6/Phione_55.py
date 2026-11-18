from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="346448a1-4e2a-59ca-909d-fdb3344564bd",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phione.Name",
    display_name="Phione",
    searchable_by=["Phione", "Basic", "Phione"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=489,
    abilities=[
        Attack(
            title="Beckon",
            game_text="Put a Supporter card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Energy Press",
            game_text="This attack does 20 damage for each Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)