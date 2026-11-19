from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.trainers import named
from ptcgo.game.session.effects import is_trainer_card
from ptcgo.game.card_effects.trainers import all_of

card = PokemonCardDef(
    guid="29b73313-1fab-5e31-9822-260ceffcacda",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Relicanth.Name",
    display_name="Relicanth",
    searchable_by=["Relicanth", "Basic", "Relicanth"],
    subtypes=["Basic"],
    collector_number=51,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=369,
    abilities=[
        Attack(
            title="Primal Calling",
            game_text="Search your deck for up to 3 Trainer Cards that have Fossil in their names, show them to your opponent, and put them into your hand. Shuffle your deck afterward.",
            cost={},
            effect=search_to_hand(all_of(is_trainer_card, named("fossil")), count=3, reveal=True),
        ),
        Attack(
            title="Sleep Swirl",
            game_text="Both Relicanth and the Defending Pok\u00e9mon are now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)