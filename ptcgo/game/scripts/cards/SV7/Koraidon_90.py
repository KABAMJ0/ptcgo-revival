from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.trainers import is_pokemon_ex
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="bfbd60cc-c58f-5f05-9a63-685319248c41",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Koraidon.Name",
    display_name="Koraidon",
    searchable_by=["Koraidon", "Basic", "Koraidon"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=1007,
    abilities=[
        Attack(
            title="Resolute Fang",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex, this attack does 70 more damage.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_pokemon_ex(ctx.defender), 70),
        ),
    ],
)