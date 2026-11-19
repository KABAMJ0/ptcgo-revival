from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, is_basic_energy_card

card = PokemonCardDef(
    guid="21330aa5-c6c0-501a-94e5-5ad94cd0db91",
    key="SWSH45SV",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DittoV.Name",
    display_name="Ditto V",
    searchable_by=["Ditto V", "Basic", "V", "DittoV"],
    subtypes=["Basic", "V"],
    collector_number=118,
    set_code="SWSH45SV",
    rarity=Rarities.RareHoloV,
    hp=170,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=132,
    abilities=[
        Ability(
            title="V Transformation",
            game_text="Once during your turn, you may choose a Basic Pok\u00e9mon V from your discard pile and switch it with this Pok\u00e9mon. Any attached cards, damage counters, Special Conditions, turns in play, and any other effects remain on the new Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Stick On",
            game_text="Attach a basic Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=attach_from_discard(is_basic_energy_card, count=1, target="self"),
        ),
    ],
)