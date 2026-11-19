from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="11d6364b-316f-5863-bbc8-e75c1ad5ece5",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesScraggy.Name",
    display_name="Marnie's Scraggy",
    searchable_by=["Marnie's Scraggy", "Basic", "MarniesScraggy"],
    subtypes=["Basic"],
    collector_number=132,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=559,
    abilities=[
        Attack(
            title="Crunch",
            game_text="Discard an Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=discard_opponent_energy_attack(1),
        ),
    ],
)