from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_attach_energy


card = PokemonCardDef(
    guid="5f1f1f1a-37d8-5c53-bfb4-076d7a321919",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizarex.Name",
    display_name="Cyclizar ex",
    searchable_by=["Cyclizar ex", "Basic", "ex", "Cyclizarex"],
    subtypes=["Basic", "ex"],
    collector_number=18,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=967,
    abilities=[
        Attack(
            title="Power Run",
            game_text="Search your deck for a Basic Energy card and attach it to this Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=search_attach_energy(predicate=is_basic_energy_card, count=1, to_self=True),
        ),
        Attack(
            title="Full Throttle",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=lock_self_attack(),
        ),
    ],
)