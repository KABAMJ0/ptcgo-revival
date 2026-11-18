from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="f2bb927d-a029-58aa-9846-b7ebdef44b38",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name",
    display_name="Tangela",
    searchable_by=["Tangela", "Basic", "Tangela"],
    subtypes=["Basic"],
    collector_number=44,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=114,
    abilities=[
        Ability(
            title="Reactive Healing",
            game_text="Whenever you attach a React Energy card from your hand to Tangela, remove all damage counters from Tangela.",
            effect=unimplemented,
        ),
        Attack(
            title="Entangling Vines",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, that Pok\u00e9mon can't attack during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=unimplemented,
        ),
        Attack(
            title="Gentle Wrap",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=no_retreat_attack(),
        ),
    ],
)