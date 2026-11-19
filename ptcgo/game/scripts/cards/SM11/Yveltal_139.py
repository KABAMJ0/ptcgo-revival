from ptcgo.game.card_effects.attacks_common import bonus_if, stadium_in_play_cond
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import bonus_if, stadium_in_play_cond

card = PokemonCardDef(
    guid="c90c8df5-ee10-5535-b810-9516d9f52904",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name",
    display_name="Yveltal",
    searchable_by=["Yveltal", "Basic", "Yveltal"],
    subtypes=["Basic"],
    collector_number=139,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=717,
    abilities=[
        Attack(
            title="Blow Through",
            game_text="If there is any Stadium card in play, this attack does 20 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(stadium_in_play_cond, 20),
        ),
        Attack(
            title="Shadow Impact",
            game_text="Put 3 damage counters on 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)