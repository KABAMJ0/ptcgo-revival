from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.card_effects.attacks_common import flip_gate
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e25c9225-422d-522c-aff8-23357a105457",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magby.Name",
    display_name="Magby",
    searchable_by=["Magby", "Baby", "Magby"],
    subtypes=["Baby"],
    collector_number=17,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=30,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=240,
    abilities=[
        Attack(
            title="Energy Catch",
            game_text="Flip a coin. If heads, put a basic Energy card from your discard pile into your hand.",
            cost={PokemonTypes.FIRE: 1},
            effect=flip_gate(recover_from_discard(is_basic_energy_card, count=1, to="hand")),
        ),
    ],
)