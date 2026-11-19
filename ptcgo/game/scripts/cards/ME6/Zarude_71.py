from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="680bede1-fd6f-5451-82d7-3aed089ffc00",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic", "Zarude"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=893,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
        Attack(
            title="Deadly Whip",
            game_text="Flip 2 coins. If both of them are heads, this attack does 150 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=flip_damage(coins=2, require_all=True, base=50, bonus=150),
        ),
    ],
)