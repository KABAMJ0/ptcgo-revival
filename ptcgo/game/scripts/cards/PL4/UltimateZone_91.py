from ptcgo.game.data_utils import StadiumCardDef, Ability, Activations
from ptcgo.game.attributes import Rarities
from ptcgo.game.card_effects.support_common import move_bench_energy_to_named_active


_effect, _condition = move_bench_energy_to_named_active("Arceus")


card = StadiumCardDef(
    guid="b7f26af1-2eae-50c2-9563-c798e7f462b0",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltimateZone.Name",
    display_name="Ultimate Zone",
    searchable_by=["Ultimate Zone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    ability=Ability(
        title="Ultimate Zone",
        game_text="During each player's turn, the player may move an Energy card attached to 1 of his or her Benched Pok\u00e9mon to his or her Active Arceus as often as he or she likes.",
        activation=Activations.UNLIMITED,
        effect=_effect,
        condition=_condition,
    ),
)
