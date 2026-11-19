from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_random_hand_attack

card = PokemonCardDef(
    guid="3b630a79-f4fc-50c5-ba30-22560a987b22",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name",
    display_name="Mienfoo",
    searchable_by=["Mienfoo", "Basic", "Mienfoo"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=619,
    abilities=[
        Attack(
            title="Knock Off",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=discard_random_hand_attack(count=1),
        ),
    ],
)