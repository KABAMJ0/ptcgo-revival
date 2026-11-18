from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="6b24a807-dec6-50fb-b088-67999e6fade3",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansPichu.Name",
    display_name="Ethan's Pichu",
    searchable_by=["Ethan's Pichu", "Basic", "EthansPichu"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Attack(
            title="Zapping Draw",
            game_text="Draw a card.",
            cost={},
            damage=30,
            effect=draw_attack(1),
        ),
    ],
)