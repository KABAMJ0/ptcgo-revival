from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import draw_attack

card = PokemonCardDef(
    guid="ac6573fa-7d65-5f9c-97a4-47282f97c1ca",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name",
    display_name="Mimikyu",
    searchable_by=["Mimikyu", "Basic", "Mimikyu"],
    subtypes=["Basic"],
    collector_number=112,
    set_code="SM9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Attack(
            title="Filch",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=draw_attack(2),
        ),
        Attack(
            title="Copycat",
            game_text="If your opponent's Pok\u00e9mon used an attack that isn't a GX attack during their last turn, use it as this attack.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)