from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, flip_damage

card = PokemonCardDef(
    guid="9db0064c-af16-5950-acce-c84086852587",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Houndoom"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="NEO3",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=229,
    abilities=[
        Attack(
            title="Dark Flame",
            game_text="Discard 1 Fire Energy card attached to Houndoom or this attack does nothing. If there are any Darkness Energy cards in your discard pile, attach 1 of them to Houndoom.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Black Fang",
            game_text="Flip a number of coins equal to the number of Darkness Energy attached to Houndoom. This attack does 30 damage plus 10 more damage for each heads.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=flip_damage(coins_from=count_energy("self", PokemonTypes.DARKNESS), base=30, per_heads=10),
        ),
    ],
)