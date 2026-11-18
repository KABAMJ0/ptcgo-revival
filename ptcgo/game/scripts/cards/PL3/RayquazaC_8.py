from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_for_bonus
from ptcgo.game.card_effects.trainers import is_energy_card

card = PokemonCardDef(
    guid="153a3603-8c56-5cb6-9247-493e09256646",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaC.Name",
    display_name="Rayquaza C",
    searchable_by=["Rayquaza C", "Basic", "SP", "RayquazaC"],
    subtypes=["Basic", "SP"],
    collector_number=8,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=384,
    abilities=[
        Attack(
            title="Trash Burst",
            game_text="You may discard up to 5 Energy cards from your hand. If you do, this attack does 10 damage plus 10 more damage for each Energy card you discarded.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=discard_for_bonus(predicate=is_energy_card, max_count=5, per=10, base=10),
        ),
        Attack(
            title="Twister",
            game_text="Flip 2 coins. If both are tails, this attack does nothing. For each heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            effect=unimplemented,
        ),
    ],
)