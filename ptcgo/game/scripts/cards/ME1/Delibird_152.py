from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand

card = PokemonCardDef(
    guid="ead527f1-c3bb-5f5b-8420-bafbc1365cd1",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delibird.Name",
    display_name="Delibird",
    searchable_by=["Delibird", "Basic", "Delibird"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=225,
    abilities=[
        Attack(
            title="Quick Gift",
            game_text="If you go first, you can use this attack during your first turn. Search your deck for a card and put it into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=search_to_hand(None, count=1, reveal=False),
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)