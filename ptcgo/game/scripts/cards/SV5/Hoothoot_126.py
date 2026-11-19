from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import reveal_hand_attack

card = PokemonCardDef(
    guid="c3e934d6-b996-5d73-97e1-87715b155c58",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    display_name="Hoothoot",
    searchable_by=["Hoothoot", "Basic", "Hoothoot"],
    subtypes=["Basic"],
    collector_number=126,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=163,
    abilities=[
        Attack(
            title="Silent Wing",
            game_text="Your opponent reveals their hand.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=reveal_hand_attack(),
        ),
    ],
)