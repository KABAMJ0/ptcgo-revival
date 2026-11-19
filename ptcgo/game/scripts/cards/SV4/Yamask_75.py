from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import place_counters

card = PokemonCardDef(
    guid="d1e9bca4-94a5-52f6-95dd-45c4654d80f1",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    display_name="Yamask",
    searchable_by=["Yamask", "Basic", "Yamask"],
    subtypes=["Basic"],
    collector_number=75,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=562,
    abilities=[
        Attack(
            title="Ominous Eyes",
            game_text="Put 3 damage counters on 1 of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=place_counters(3, target="choose_any_opponent"),
        ),
    ],
)