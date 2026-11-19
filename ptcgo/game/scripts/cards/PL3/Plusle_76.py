from ptcgo.game.card_effects.support_common import attach_from_hand
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6fbe7b43-e49a-564d-8b2e-997d0b9c46ea",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Plusle.Name",
    display_name="Plusle",
    searchable_by=["Plusle", "Basic", "Plusle"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="PL3",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=311,
    abilities=[
        Attack(
            title="Greedy Draw",
            game_text="If you have the same number of cards or less in your hand as your opponent, draw cards until you have 1 more card than your opponent. (If you have more cards in your hand than your opponent, this attack does nothing.)",
            cost={},
            effect=attach_from_hand(basic_energy_of("lightning"), count=1, target="choice"),
        ),
        Attack(
            title="Hand Charge",
            game_text="Attach a Lightning Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)