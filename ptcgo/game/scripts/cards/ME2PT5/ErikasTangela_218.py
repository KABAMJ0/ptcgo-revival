from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import named
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="df7a44e8-21ef-5964-a79e-cfceeb29dc02",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasTangela.Name",
    display_name="Erika's Tangela",
    searchable_by=["Erika's Tangela", "Basic", "ErikasTangela"],
    subtypes=["Basic"],
    collector_number=218,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=114,
    abilities=[
        Ability(
            title="Gathering of Blossoms",
            game_text="Once during your turn, you may use this Ability. Search your deck for an Erika's Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(named("erika's"), count=1, reveal=True),
        ),
        Attack(
            title="Bind",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)