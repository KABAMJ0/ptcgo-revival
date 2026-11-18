from ptcgo.game.card_effects.support_common import move_bench_energy_to_named_active
from ptcgo.game.content.definitions import Ability, Activations
from ptcgo.game.data_utils import StadiumCardDef
from ptcgo.game.attributes import Rarities

_effect, _condition = move_bench_energy_to_named_active("Arceus")

card = StadiumCardDef(
    guid="05e5d4af-b11f-5bdf-8166-b427833da3e4",
    key="DPP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltimateZone.Name",
    display_name="Ultimate Zone",
    searchable_by=["Ultimate Zone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=55,
    set_code="DPP",
    rarity=Rarities.RarePromo,
    ability=Ability(
        title="Ultimate Zone",
        game_text="During each player's turn, the player may move an Energy card attached to 1 of his or her Benched Pok\u00e9mon to his or her Active Arceus as often as he or she likes.",
        activation=Activations.UNLIMITED,
        effect=_effect,
        condition=_condition,
    ),
)
