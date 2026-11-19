from ptcgo.game.card_effects.support_common import switch_self_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import switch_self_attack

card = PokemonCardDef(
    guid="72bc314e-a050-5460-ab32-6517411fe25d",
    key="SWSH9TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RapidStrikeUrshifuV.Name",
    display_name="Rapid Strike Urshifu V",
    searchable_by=["Rapid Strike Urshifu V", "Basic", "V", "Rapid Strike", "RapidStrikeUrshifuV"],
    subtypes=["Basic", "V", "Rapid Strike"],
    collector_number=20,
    set_code="SWSH9TG",
    rarity=Rarities.RareHoloV,
    hp=220,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=892,
    abilities=[
        Attack(
            title="Strafe",
            game_text="You may switch this Pok\u00e9mon with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=switch_self_attack(optional=True),
        ),
        Attack(
            title="Hundred Furious Blows",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
        ),
    ],
)