from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_gate, random_card_to_deck

card = PokemonCardDef(
    guid="56a631f7-67e8-5dc3-987c-74dcb0ec232c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndstone.Name",
    display_name="Houndstone",
    searchable_by=["Houndstone", "Stage 1", "Houndstone"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name",
    family_id=971,
    abilities=[
        Attack(
            title="Horrifying Bite",
            game_text="Flip a coin until you get tails. For each heads, choose a random card from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)