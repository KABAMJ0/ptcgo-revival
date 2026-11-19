from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="42eaf839-c876-517d-a8ee-9bd06c983431",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name",
    display_name="Gastly",
    searchable_by=["Gastly", "Basic", "Gastly"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=92,
    abilities=[
        Attack(
            title="Mysterious Beam",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=flip_discard_opponent_energy(),
        ),
        Attack(
            title="Suffocating Gas",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
        ),
    ],
)