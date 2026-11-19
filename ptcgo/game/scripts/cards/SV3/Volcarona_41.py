from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import attach_from_discard
from ptcgo.game.card_effects.trainers import basic_energy_of, is_basic_energy_card

card = PokemonCardDef(
    guid="691bfab2-289f-5529-8e31-ad863c44e23d",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Volcarona"],
    subtypes=["Stage 1"],
    collector_number=41,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Attack(
            title="Flame Cloak",
            game_text="Attach a Basic Fire Energy card from your discard pile to this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            effect=attach_from_discard(basic_energy_of("fire"), count=1, target="self"),
        ),
        Attack(
            title="Heat Blast",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)