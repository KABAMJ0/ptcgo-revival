from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import attach_from_hand

LIGHTNING = PokemonTypes.LIGHTNING.value


def _is_lightning_energy(card):
    return energy_provides_type(card, LIGHTNING)


card = PokemonCardDef(
    guid="c4ba181d-e00f-5814-9a58-9a894adb60b6",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pachirisu.Name",
    display_name="Pachirisu",
    searchable_by=["Pachirisu", "Basic", "Pachirisu"],
    subtypes=["Basic"],
    collector_number=18,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=417,
    abilities=[
        Ability(
            title="Self-Generation",
            game_text="Once during your turn, when you put Pachirisu from your hand onto your Bench, you may attach up to 2 Lightning Energy cards from your hand to Pachirisu.",
            trigger=Triggers.ON_PLAY,
            effect=unimplemented,
        ),
        Attack(
            title="Shocking Bolt",
            game_text="Put all Energy cards attached to Pachirisu in the Lost Zone.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=50,
            effect=unimplemented,
        ),
    ],
)