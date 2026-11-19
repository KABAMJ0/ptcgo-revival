from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import cure_conditions_effect

card = PokemonCardDef(
    guid="e17ff6d2-236e-54c1-8259-d225e9d86795",
    key="ME55",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name",
    display_name="Pikachu",
    searchable_by=["Pikachu", "Basic", "Pikachu"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="ME55",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=25,
    abilities=[
        Attack(
            title="Get Some Air",
            game_text="This Pok\u00e9mon recovers from all Special Conditions.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=cure_conditions_effect(scope="active"),
        ),
        Attack(
            title="Smash Kick",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)