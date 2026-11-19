from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.trainers import is_pokemon_ex
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5194286a-d768-5c98-b8e8-693f9c79d174",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Moltres.Name",
    display_name="Moltres",
    searchable_by=["Moltres", "Basic", "Moltres"],
    subtypes=["Basic"],
    collector_number=14,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=146,
    abilities=[
        Attack(
            title="Fighting Wings",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon ex, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_pokemon_ex(ctx.defender), 90),
        ),
    ],
)