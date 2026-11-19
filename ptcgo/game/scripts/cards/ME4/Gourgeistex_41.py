from ptcgo.game.card_effects.attacks_common import discard_random_hand_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="79f0dadb-a447-51f4-93cc-2b18d2348a46",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gourgeistex.Name",
    display_name="Gourgeist ex",
    searchable_by=["Gourgeist ex", "Stage 1", "ex", "Gourgeistex"],
    subtypes=["Stage 1", "ex"],
    collector_number=41,
    set_code="ME4",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name",
    family_id=710,
    abilities=[
        Attack(
            title="Horrifying Rondo",
            game_text="This attack does 50 more damage for each of your Benched Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Ghostly Touch",
            game_text="Discard a random card from your opponent's hand.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=140,
            effect=discard_random_hand_attack(1),
        ),
    ],
)