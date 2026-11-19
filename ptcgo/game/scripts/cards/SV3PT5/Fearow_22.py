from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="94c3ef74-249a-57f0-87a5-b582c5704054",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Fearow.Name",
    display_name="Fearow",
    searchable_by=["Fearow", "Stage 1", "Fearow"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spearow.Name",
    family_id=21,
    abilities=[
        Attack(
            title="Beak Catch",
            game_text="Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(None, count=3, minimum=0, reveal=False),
        ),
        Attack(
            title="Speed Dive",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)