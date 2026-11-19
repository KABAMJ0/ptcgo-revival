from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import composed
from ptcgo.game.card_effects.support_common import search_to_hand, switch_self_attack

card = PokemonCardDef(
    guid="8a932946-7973-545b-8d97-3715f42a2024",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiri.Name",
    display_name="Tatsugiri",
    searchable_by=["Tatsugiri", "Basic", "Tatsugiri"],
    subtypes=["Basic"],
    collector_number=141,
    set_code="SV4",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=978,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Survival Strategy",
            game_text="Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck. You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=composed(
                search_to_hand(None, count=2, minimum=0, reveal=False),
                then=switch_self_attack(0, optional=True),
            ),
        ),
    ],
)