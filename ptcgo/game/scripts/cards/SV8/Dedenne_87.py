from ptcgo.game.card_effects.support_common import recover_from_discard
from ptcgo.game.session.effects import is_trainer_card
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
card = PokemonCardDef(
    guid="06890406-daf9-5a73-847e-b2e207d930c8",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=702,
    abilities=[
        Attack(
            title="Electromagnetic Sonar",
            game_text="Put a Trainer card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=recover_from_discard(is_trainer_card, count=1, to="hand"),
        ),
        Attack(
            title="Gnaw",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
        ),
    ],
)