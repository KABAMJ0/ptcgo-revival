from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.session.effects import is_pokemon_card
from ptcgo.game.card_effects.attacks_common import flip_bonus

card = PokemonCardDef(
    guid="6f147a98-0ecd-50af-a980-86c9ae3fe08f",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Furret.Name",
    display_name="Furret",
    searchable_by=["Furret", "Stage 1", "Furret"],
    subtypes=["Stage 1"],
    collector_number=21,
    set_code="HGSS1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sentret.Name",
    family_id=161,
    abilities=[
        Attack(
            title="Find a Friend",
            game_text="Search your deck for a Pok\u00e9mon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(is_pokemon_card, count=1, reveal=True),
        ),
        Attack(
            title="Quick Blow",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)