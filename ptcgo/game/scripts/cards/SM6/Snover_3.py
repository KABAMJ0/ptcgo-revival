from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.patterns import is_pokemon_of_type
from ptcgo.game.card_effects.attacks_common import bonus_if

card = PokemonCardDef(
    guid="7fafa0ec-4ea1-5453-9710-073353b79460",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Snover.Name",
    display_name="Snover",
    searchable_by=["Snover", "Basic", "Snover"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="SM6",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=459,
    abilities=[
        Attack(
            title="Ice Shard",
            game_text="If your opponent's Active Pok\u00e9mon is a Fighting Pok\u00e9mon, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=bonus_if(lambda ctx: ctx.defender is not None and is_pokemon_of_type(ctx.defender, "fighting"), 40),
        ),
    ],
)