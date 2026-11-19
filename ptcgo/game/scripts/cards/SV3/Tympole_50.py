from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_discard_opponent_energy

card = PokemonCardDef(
    guid="8093bd8c-f7a9-590d-9bb7-706d73df0a17",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    display_name="Tympole",
    searchable_by=["Tympole", "Basic", "Tympole"],
    subtypes=["Basic"],
    collector_number=50,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=535,
    abilities=[
        Attack(
            title="Screw Tail",
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=flip_discard_opponent_energy(),
        ),
    ],
)